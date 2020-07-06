# Hugo Orbit Theme

This is a Hugo port of [Orbit](//github.com/xriley/Orbit-Theme) - great looking resume/CV template designed for developers by Xiaoying Riley.

## Screenshot

![Orbit screenshot](https://raw.githubusercontent.com/aerohub/hugo-orbit-theme/master/images/screenshot.png)

## Features

### Original

- Fully Responsive
- HTML5 + CSS3
- Built on Bootstrap 3
- 6 Color Schemes
- FontAwesome icons
- **LESS** files included
- Compatible with all modern browsers

### Added

- Support for Google Analytics
- Print format improvements with option to generate PDF (further information below)
- Feature for sidebar on the left side

## Demo

You can see it in action on [Hugo Themes site](http://themes.gohugo.io/theme/hugo-orbit-theme/).

## Contents

- [Installation](#installation)
- [Configuration](#configuration)
    - [Test your site](#test-your-site)
	- [Build your site](#build-your-site)
- [Generate a PDF version](#generate-a-pdf-version)
- [Contributing](#contributing)
- [License](#license)


## Installation

Inside the folder of your new Hugo site run:

    $ cd themes
    $ git clone https://github.com/aerohub/hugo-orbit-theme

Copy the default contents for a Quick-Start:

    $ cp -r hugo-orbit-theme/exampleSite/* ../

For more information read the official [Hugo setup guide](//gohugo.io/overview/installing/).


## Configuration

Open your just-copied `config.toml` and fill it with your data. All the page content may be configured throw one file.

### Test your site

In order to see your site in action, run Hugo's built-in local server.

    $ hugo server

Now enter `localhost:1313` in the address bar of your browser.

### Build your site

Just run

	$ hugo

You'll find your resume files in `public` folder in the root of Hugo project.


## Generate a PDF version

Although there is a free Sketch template provided by [@xriley](https://github.com/xriley) ([Link](https://themes.3rdwavemedia.com/resources/sketch-template/orbit-sketch-sketch-resume-template-for-developers/)), you might do not want to write / copy & paste the contents again and / or don't have access to a Mac with the Sketch program.

[@Lednerb](https://github.com/Lednerb/) discovered the following way to generate PDFs with this theme in an easy way for developers as follows:

1. Finish the website
2. Within Chromium / Chrome: `CTRL+P` (Print), change settings to borderless, only the first page and printer to "Save as PDF"
3. `CTRL+SHIFT+I` to open the development panel
4. Remove contents in the sidebar and the already saved sections, maybe also sections that should not be placed on the second page
5. Repeat step 2 to save the next page as a new document
6. Reload the site, repeat steps 4 and 5 until all pages are saved
7. Use a tool like `pdfunite` to merge the different PDF files / pages into one file
8. You can add the generated file to the downloads section if you like


## Contributing

Did you found a bug or got an idea? Feel free to use the [issue tracker](//github.com/aerohub/hugo-orbit-theme/issues) or directly create a [pull request](//github.com/aerohub/hugo-orbit-theme/pulls).


## License

The original template is released under the Creative Commons Attribution 3.0 License. Please keep the original attribution link when using for your own project. If you'd like to use the template without the attribution, you can check out other license options via the template author's website: themes.3rdwavemedia.com
