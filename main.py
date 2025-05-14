import sys
from core.app import PythonSuiteDesignerApp

def main():
    app = PythonSuiteDesignerApp(sys.argv)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
