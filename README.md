## Ye-rm

A CLI tool to remove all songs by a specific artist from a Spotify playlist.

## Inspiration

Artists earn money from Spotify royalties when their songs are played. This tool is a way to remove all of their songs from your playlists to deprive them of that revenue, so you don't need to worry about accidentally supporting an artist you no longer align with when listening on shuffle :).

### Usage

#### Install dependencies
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    export PYTHONPATH=$PYTHONPATH:$(pwd)

#### Set up Environment Variables
    # for the spotipy library
    export SPOTIPY_CLIENT_ID=<your-spotify-client-id>
    export SPOTIPY_CLIENT_SECRET=<your-spotify-client-secret>
    export SPOTIPY_REDIRECT_URI='http://localhost:8080'

    # for the CLI
    export SPOTIFY_USER_ID=<your-spotify-user-id>

#### Run the CLI

    python ye_rm/cli.py <artist-name>

Example:

     python ye_rm/cli.py "Kanye West"

You will be redirected to a web page that will ask you to approve the application and login.

##### Results

The CLI will print the songs/playlists that have been removed.

    Report for ye-rm Kanye West
    Playlist: summer 2k18
        Song Removed: All We Got (feat. Kanye West & Chicago Children's ...
    Playlist: UPBEAT
        Song Removed: Follow God
    Playlist: Vibez
        Song Removed: All We Got (feat. Kanye West & Chicago Children's ...
    Playlist: Rap Jams
        Song Removed: Gold Digger
        Song Removed: All Falls Down
        Song Removed: Hey Mama
    Playlist: porch music
        Song Removed: Wouldn't You Like To…
        Song Removed: Erase Me - Main

*Note: The CLI will only remove songs from playlists that you have access to.*


### Spotify API

#### Get your Spotify API credentials

For information on getting SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI, see the [Spotify API documentation](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).

You will need to [create an app](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app) and set the redirect URI to `http://localhost:8080`.

#### Get your Spotify user ID

You can find your spotify user id by going to the [Spotify profile page](https://www.spotify.com/us/account/profile/) and clicking `Edit profile`.

[Here](https://community.spotify.com/t5/Accounts/How-do-you-find-your-own-user-ID/td-p/5270104) is a related post from the Spotify Community about how to find your user ID.

