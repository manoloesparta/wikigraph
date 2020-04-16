<p align="center">
  <a>
    <img width="200px" src="logo.png" alt="Wikigraph" />
    <h1 align="center">Wikigraph</h1>
  </a>
</p>

<p align="center">
  <a><img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version"></a>
  <a><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License"></a>
  <a><img src="https://img.shields.io/badge/Made%20with-C%2B%2B-ff69b4" alt="C++"></a>
  <a><img src="https://img.shields.io/badge/Made%20with-Python-blue" alt="Python"></a>
</p>

> How far is X article from Y article?

This program was inspired on how far is the Mexico wikipedia article from any other article through clicking other hyperlinks. The implementation was made in two parts, the first one is web scrapper made with python that will download all the hyperlinks in a wikipedia article and store them in a file with named with the title of the article.

## Requirements
```
g++
cmake
python3 & pip
```

## Run it locally
In order to scrap wikipedia articles you should
```
pip instal -r requirements.txt
python collect.py
```

And to search
```
mkdir build && cd build
cmake ..
make
./wiki
```

## Contributing
Feel free to make pull requests. Check out the issues tab in order to see what's pending

## License
This project is under the MIT License