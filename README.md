## About

This is the source of my blog, hosted at [sharats.me](http://sharats.me). It is powered by
[Hugo](https://gohugo.io) and articles are written in Markdown.

The theme is a modified version of the `nofancy` theme.

All code for generation of the blog (that is written by me) is licensed with the
[MIT License](http://mitl.sharats.me).

To build, install Hugo and issue `make build` or to serve locally, `make serve`.

If you find any error (*e.g.,* typos) or bugs, please open an issue or send a PR to fix. I'll be
very greatful.

## Usage

Create a new post in markdown with:

    hugo new posts/my-new-post.md

Start a live server with:

    make serve

Build static site with:

    make build

## Deployment

Site is deployed on Netlify. The environment variable `HUGO_VERSION` should be set to the correct
Hugo version. Build command used is `make`.
