import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import argparse
from typing import Generator
from dataclasses import dataclass

from ye_rm.api import SpotifyAPIRemover


def main():
    parser = argparse.ArgumentParser(description='Remove songs by specific artist from a Spotify playlist')
    parser.add_argument('artist_name', help='Artist name to remove', type=str)
    args = parser.parse_args()
    user_id = os.getenv("SPOTIFY_USER_ID")
    SpotifyAPIRemover(args.artist_name, user_id).ye_rm()

if __name__ == "__main__":
    main()