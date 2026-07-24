"""
SentinelAI
Main Window

This module contains the primary application window.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Primary application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("SentinelAI")
        self.resize(1400, 900)

        self._build_ui()

    def _build_ui(self) -> None:
        """Build the application interface."""

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # ------------------------
        # Sidebar
        # ------------------------

        sidebar = QFrame()
        sidebar.setFixedWidth(220)

        sidebar.setStyleSheet("""
            QFrame {
                background-color: #202225;
            }

            QPushButton {
                color: white;
                background: transparent;
                border: none;
                text-align: left;
                padding: 12px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #2f3136;
            }

            QPushButton:pressed {
                background-color: #3b3e45;
            }
        """)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 15, 10, 15)

        title = QLabel("SentinelAI")
        title.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
            padding-bottom: 20px;
        """)

        sidebar_layout.addWidget(title)

        self.dashboard_button = QPushButton("🏠 Dashboard")
        self.review_button = QPushButton("📝 Code Review")
        self.settings_button = QPushButton("⚙ Settings")

        sidebar_layout.addWidget(self.dashboard_button)
        sidebar_layout.addWidget(self.review_button)
        sidebar_layout.addWidget(self.settings_button)

        sidebar_layout.addStretch()

        version = QLabel("Version 0.1.0")
        version.setStyleSheet("color: gray;")
        sidebar_layout.addWidget(version)

        layout.addWidget(sidebar)

        # ------------------------
        # Pages
        # ------------------------

        self.pages = QStackedWidget()

        self.dashboard_page = self._create_page(
            "Dashboard",
            "Welcome to SentinelAI"
        )

        self.review_page = self._create_page(
            "AI Code Review",
            "Review source code with AI."
        )

        self.settings_page = self._create_page(
            "Settings",
            "Configure SentinelAI."
        )

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.review_page)
        self.pages.addWidget(self.settings_page)

        layout.addWidget(self.pages)

        # ------------------------
        # Status Bar
        # ------------------------

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

        # ------------------------
        # Signals
        # ------------------------

        self.dashboard_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(0)
        )

        self.review_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(1)
        )

        self.settings_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(2)
        )

    @staticmethod
    def _create_page(title: str, subtitle: str) -> QWidget:
        """Create a simple page."""

        page = QWidget()

        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        heading = QLabel(title)
        heading.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
        """)

        text = QLabel(subtitle)
        text.setStyleSheet("""
            font-size:16px;
            color:gray;
        """)

        layout.addWidget(heading)
        layout.addWidget(text)

        return page