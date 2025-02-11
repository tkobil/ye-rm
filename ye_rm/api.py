import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import Generator
from dataclasses import dataclass
from collections import defaultdict
from termcolor import colored
import logging

from ye_rm.track import Track
from ye_rm.playlist import Playlist

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SpotifyAPIRemover:
    def __init__(self, artist_name: str, user_id: str):
        self.artist_name = artist_name
        self.sp = self._setup_spotify_client()
        self.user_id = user_id
        self.batch_rm_limit = 100

    @staticmethod
    def _setup_spotify_client() -> spotipy.Spotify:
        """Initialize Spotify client with necessary permissions"""
        auth_manager = SpotifyOAuth(scope="playlist-modify-public playlist-modify-private")
        return spotipy.Spotify(auth_manager=auth_manager)
    
    def ye_rm(self) -> None:
        report: dict[Playlist, list[Track]] = defaultdict(list)
        logger.info(f"fetching playlists...")
        for playlist in self._get_playlists():
            batch: list[Track] = []
            logger.info(f"fetching tracks from {playlist.name}...")
            for track in self._get_tracks_from_playlist(playlist.id):
                batch.append(track)
                if len(batch) == self.batch_rm_limit:
                    logger.info(f"Removing {len(batch)} tracks from {playlist.id}")
                    report[playlist] += self._safe_remove(playlist, batch)
                    batch = []
            
            if batch:
                logger.info(f"Removing {len(batch)} tracks from {playlist.id}")
                report[playlist] += self._safe_remove(playlist, batch)
        
        self._print_report(report)

    
    def _safe_remove(self, playlist: Playlist, batch: list[Track]) -> list[Track]:
        try:
            self.sp.playlist_remove_all_occurrences_of_items(playlist.id, [track.id for track in batch])
        except Exception as e:
            print(f"Error removing tracks from {playlist.id}: {e}")
            return []
        
        return batch

    
    def _print_report(self, report: dict[Playlist, list[Track]]) -> None:
        title = colored(f"Report for ye-rm {self.artist_name}", "green")
        print(title)

        pretty_dict = ''
        
        for k, v in report.items():
            pretty_dict += colored(f'Playlist: {k.name}\n', "green")
            for value in v:
                pretty_name = value.name[:50] + '...' if len(value.name) > 50 else value.name
                pretty_dict += colored(f'    Song Removed: {pretty_name}\n', "red")

        print(pretty_dict)

    
    def _get_tracks_from_playlist(self, playlist_id) -> Generator[Track, None, None]:
        results = self.sp.playlist_tracks(playlist_id)
        while results:
            current_results = results
            results = self.sp.next(results) if results['next'] else None

            for item in current_results['items']:
                artists = [artist['name'].lower() for artist in item['track']['artists']]
                if self.artist_name.lower() in artists:
                    yield Track(item['track']['name'], artists, item['track']['id'], item['track']['uri'])

    def _get_playlists(self) -> Generator[Playlist, None, None]:
        playlists = self.sp.user_playlists(self.user_id)
        while playlists:
            current_playlists = playlists
            playlists = self.sp.next(playlists) if playlists['next'] else None

            for playlist in current_playlists['items']:
                yield Playlist(playlist['id'], playlist['name'])
