#!/usr/bin/env python3
"""
GrowFit - Main entry point

Simple entry point script for running the GrowFit application.
This provides an easy way to launch the app without needing to navigate
to the growfit package directory.
"""

if __name__ == "__main__":
    from growfit.app import run_app
    run_app()