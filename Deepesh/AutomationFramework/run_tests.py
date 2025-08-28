#!/usr/bin/env python3
"""
OrangeHRM Test Runner Script
This script provides an easy way to run different test suites and configurations.
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Command executed successfully!")
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with exit code {e.returncode}")
        if e.stdout:
            print("Stdout:")
            print(e.stdout)
        if e.stderr:
            print("Stderr:")
            print(e.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='OrangeHRM Test Runner')
    parser.add_argument('--mode', choices=['all', 'smoke', 'admin', 'leave', 'maintenance', 'integration', 'performance'], 
                       default='smoke', help='Test execution mode')
    parser.add_argument('--parallel', action='store_true', help='Run tests in parallel')
    parser.add_argument('--html-report', action='store_true', help='Generate HTML report')
    parser.add_argument('--coverage', action='store_true', help='Generate coverage report')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Change to the framework directory
    framework_dir = Path(__file__).parent
    os.chdir(framework_dir)
    
    print("🏢 OrangeHRM Automation Test Suite")
    print("=" * 50)
    
    # Build the pytest command
    cmd_parts = ["pytest"]
    
    # Add mode-specific markers
    if args.mode == 'smoke':
        cmd_parts.extend(["-m", "smoke"])
    elif args.mode == 'admin':
        cmd_parts.extend(["-m", "admin"])
    elif args.mode == 'leave':
        cmd_parts.extend(["-m", "leave"])
    elif args.mode == 'maintenance':
        cmd_parts.extend(["-m", "maintenance"])
    elif args.mode == 'integration':
        cmd_parts.extend(["-m", "integration"])
    elif args.mode == 'performance':
        cmd_parts.extend(["-m", "performance"])
    
    # Add parallel execution
    if args.parallel:
        cmd_parts.extend(["-n", "auto"])
    
    # Add HTML reporting
    if args.html_report:
        cmd_parts.extend(["--html=reports/report.html", "--self-contained-html"])
    
    # Add coverage
    if args.coverage:
        cmd_parts.extend(["--cov=.", "--cov-report=html", "--cov-report=term-missing"])
    
    # Add verbose output
    if args.verbose:
        cmd_parts.extend(["-v", "-s"])
    
    # Add test discovery
    cmd_parts.extend(["--tb=short"])
    
    # Build the final command
    command = " ".join(cmd_parts)
    
    # Create reports directory if it doesn't exist
    if args.html_report or args.coverage:
        os.makedirs("reports", exist_ok=True)
    
    # Run the tests
    success = run_command(command, f"Running {args.mode} tests")
    
    if success:
        print(f"\n🎉 {args.mode.title()} tests completed successfully!")
        
        if args.html_report:
            report_path = framework_dir / "reports" / "report.html"
            print(f"📊 HTML report generated: {report_path}")
        
        if args.coverage:
            coverage_path = framework_dir / "htmlcov" / "index.html"
            print(f"📈 Coverage report generated: {coverage_path}")
    else:
        print(f"\n💥 {args.mode.title()} tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
