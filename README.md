# \# Vietnam Adventure Publisher (VAP)

# 

# A document publishing engine that transforms a structured Microsoft Word travel manuscript into a professionally formatted handbook.

# 

# \---

# 

# \## Overview

# 

# Vietnam Adventure Publisher (VAP) is a Python-based publishing framework designed to automate the production of travel handbooks.

# 

# Instead of manually formatting hundreds of pages in Microsoft Word, VAP reads a structured DOCX manuscript, analyzes its content, detects chapters and components, and generates a publication-ready handbook with consistent styling and layout.

# 

# The project was originally created for the \*\*Vietnam Adventure 2026 Handbook\*\*, but the architecture is intended to support any structured handbook in the future.

# 

# \---

# 

# \## Objectives

# 

# \- Read Microsoft Word (.docx) manuscripts

# \- Detect chapters automatically

# \- Detect logical content components

# \- Build an in-memory handbook model

# \- Generate publication-quality Word documents

# \- Support PDF generation

# \- Support reusable publishing themes

# 

# \---

# 

# \## Features (Current)

# 

# \### Reader

# 

# \- Read DOCX files

# \- Preserve paragraph order

# \- Preserve paragraph styles

# 

# \### Parser

# 

# \- Chapter detection

# \- Component detection

# \- Handbook model generation

# 

# \### Publisher

# 

# \- Word document generation

# \- Publisher pipeline

# 

# \---

# 

# \## Planned Features

# 

# \- Hero chapter pages

# \- Automatic Table of Contents

# \- QR Code generation

# \- Image placement

# \- Tables

# \- Callout boxes

# \- Timeline layouts

# \- Maps

# \- PDF publishing

# \- Theme engine

# \- Plugin architecture

# 

# \---

# 

# \# Architecture

# 

# ```

# Input DOCX

# &#x20;    │

# &#x20;    ▼

# Document Reader

# &#x20;    │

# &#x20;    ▼

# Document Model

# &#x20;    │

# &#x20;    ▼

# Chapter Detector

# &#x20;    │

# &#x20;    ▼

# Component Detector

# &#x20;    │

# &#x20;    ▼

# Handbook Model

# &#x20;    │

# &#x20;    ▼

# Publisher

# &#x20;    │

# &#x20;    ▼

# Word Publisher

# &#x20;    │

# &#x20;    ▼

# Published Handbook

# ```

# 

# \---

# 

# \# Project Structure

# 

# ```

# vap/

# │

# ├── app/

# ├── models/

# ├── parser/

# ├── publisher/

# ├── reader/

# ├── validation/

# └── main.py

# ```

# 

# \---

# 

# \# Requirements

# 

# \- Python 3.13+ (recommended)

# \- Microsoft Word documents (.docx)

# 

# Install dependencies

# 

# ```bash

# python -m pip install -r requirements.txt

# ```

# 

# \---

# 

# \# Running

# 

# Generate Word output

# 

# ```bash

# python -m vap.main handbook.docx

# ```

# 

# Specify output

# 

# ```bash

# python -m vap.main handbook.docx -o output.docx

# ```

# 

# Generate PDF (future)

# 

# ```bash

# python -m vap.main handbook.docx --pdf

# ```

# 

# \---

# 

# \# Development Status

# 

# Current Stage

# 

# Phase 1 — Core Publisher

# 

# Completed

# 

# \- Project structure

# \- Data models

# \- CLI

# \- Reader

# 

# In Progress

# 

# \- Chapter Detector

# \- Component Detector

# \- Publisher pipeline

# 

# Planned

# 

# \- Word Publisher

# \- PDF Publisher

# \- Theme Engine

# 

# \---

# 

# \# Roadmap

# 

# \## Phase 1

# 

# \- Core document reader

# \- Chapter detection

# \- Component detection

# \- Word publishing

# 

# \## Phase 2

# 

# \- Styling

# \- Tables

# \- Images

# \- TOC

# 

# \## Phase 3

# 

# \- QR Generator

# \- Maps

# \- PDF

# \- Themes

# 

# \## Phase 4

# 

# \- Plugin system

# \- GUI

# \- Template marketplace

# 

# \---

# 

# \# License

# 

# Private Project

# 

# Copyright © 2026

# 

# Vietnam Adventure Publisher (VAP)

