from collections import deque


class SongQueue:
    def __init__(self) -> None:
        self.q = deque()
        self.is_playing = False

    def add_song(self, song) -> None:
        self.q.append(song)

    def pop_upcoming(self):
        return self.q.popleft()

    def remove_at_index(self):
        return self.q.pop()

    def empty(self):
        self.q = deque()
