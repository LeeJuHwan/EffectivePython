from abc import ABC, abstractmethod
from persistence import BookmarkDatabase
from datetime import datetime
import sys
import requests
persistence = BookmarkDatabase()


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("Commands must implement an execute method")


class AddBookmarkCommand(Command):
    """북마크 추가"""

    def execute(self, data, timestamp=None):
        data["DATE_ADDED"] = timestamp or datetime.utcnow().isoformat()
        persistence.create(data)
        return True, None


class ListBookmarksCommand:
    """데이터 조회"""

    def __init__(self, order_by="DATE_ADDED"):
        self.order_by = order_by

    def execute(self):
        return True, persistence.list(order_by=self.order_by)


class DeleteBookmarkCommand:
    """북마크 삭제"""

    def execute(self, data):
        persistence.delete(data)
        return True, None


class EditBookmarkCommand(Command):
    def execute(self, data):
        persistence.edit(data["id"], data["update"])
        return True, None


class QuitCommand:
    """프로그램 종료"""
    def execute(self):
        sys.exit()


class ImportGitHubStarsCommand:
    def _extract_bookmark_info(self, repo):
        return {
            "TITLE": repo["name"],
            "URL": repo["html_url"],
            "NOTES": repo["description"],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data["github_username"]
        next_page_of_results = f"https://api.github.com/users/{github_username}/starred"

        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"}
            )
            next_page_of_results = stars_response.links.get("next", {}).get("URL")

            for repo_info in stars_response.json():
                repo = repo_info["repo"]

                if data["preserve_timestamps"]:
                    timestamp = datetime.strptime(
                        repo_info["starred_at"], "%Y-%m-%d%T%H:%M:%SZ"
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp,
                )
        return f"Imported {bookmarks_imported} bookmarks from starred repos!"
