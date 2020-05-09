# flask-blurhash

A simple flask microservice to generate [blurhashes](https://blurha.sh)

## Install

Run `pip install -r requirements.txt`

## Run Development

Run `start-flask-blurhash.sh` while in project root folder

## Usage

The server accepts formdata with the 3 following options:

* image
    An image file to be blurhash'd, can be .png, .jpg, .jpeg, .gif

* x
    A number value for the X Coordinates for Blurhash.  Must be between 1 and 9.
    Defaults to 3 if not provided

* y
    A number value for the Y Coordinates for Blurhash.  Must be between 1 and 9.
    Defaults to 3 if not provided