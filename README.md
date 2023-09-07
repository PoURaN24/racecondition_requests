# Multithreaded HTTP/HTTPS Requester

A Python script for making HTTP/HTTPS requests simultaneously using multithreading. Created mostly in order to achieve race condition attacks. 
There is also functionality for saving the responses in order to be checked offline.

Works fine with python 3+

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a Python script that allows you to make HTTP/HTTPS requests concurrently using multithreading. 
This is created for the purpose of achieving race condition attacks. This can be especially useful for tasks like web scraping, API requests, or any other situation where you need to perform multiple HTTP requests efficiently.

## Features

- Multithreaded request execution.
- Supports both HTTP and HTTPS URLs.
- Easy-to-use command-line interface.
- Customizable request parameters such as headers, timeout, and more.
- Detailed logging for monitoring request progress.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/PoURaN24/racecondition_requests.git

2. Run it using python.. :D
