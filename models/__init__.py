#!/usr/bin/python3
"""Unique instances for the application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
