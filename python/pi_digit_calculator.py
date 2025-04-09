#!/usr/bin/env python3
"""
Pi Calculator Script - Calculates Pi digits using the Nilakantha series
and runs for a specified amount of time (default: 3 minutes)
"""

import time
import datetime
import platform
import psutil
import os
import math
import sys

def get_system_info():
    """Returns basic information about the system"""
    system_info = {
        "Platform": platform.system(),
        "Platform Release": platform.release(),
        "Platform Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": platform.node(),
        "Python Version": platform.python_version(),
        "CPU Count": psutil.cpu_count(logical=True),
        "Physical CPU Count": psutil.cpu_count(logical=False),
        "Memory (GB)": round(psutil.virtual_memory().total / (1024**3), 2)
    }
    return system_info

def calculate_pi_nilakantha(max_iterations=None, max_runtime_seconds=None):
    """
    Calculate Pi using the Nilakantha series:
    π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...
    
    Parameters:
        max_iterations: Maximum number of iterations (or None for unlimited)
        max_runtime_seconds: Maximum runtime in seconds (or None for unlimited)
    
    Returns:
        tuple: (pi_approximation, iterations, elapsed_time)
    """
    
    pi = 3.0
    operation = 1  # 1 for addition, -1 for subtraction
    denominator = 2
    iterations = 0
    start_time = time.time()
    
    # Store known PI for comparison
    true_pi = math.pi
    
    print("\nStarting Pi calculation using Nilakantha series...")
    print(f"Known value of π: {true_pi}")
    print("-" * 50)
    
    while True:
        # Check if we've reached the iteration limit
        if max_iterations is not None and iterations >= max_iterations:
            break
            
        # Check if we've reached the time limit
        if max_runtime_seconds is not None and (time.time() - start_time) >= max_runtime_seconds:
            break
        
        # Calculate the next term in the series
        term = 4 / (denominator * (denominator + 1) * (denominator + 2))
        pi += operation * term
        
        # Update variables for next iteration
        operation *= -1
        denominator += 2
        iterations += 1
        
        # Print progress every 10 seconds
        elapsed = time.time() - start_time
        current_seconds = int(elapsed)
        
        if current_seconds > 0 and current_seconds % 10 == 0 and iterations % 1000 == 0:
            # Track the last reported second to avoid multiple reports at the same second
            if not hasattr(calculate_pi_nilakantha, 'last_reported_second') or calculate_pi_nilakantha.last_reported_second != current_seconds:
                calculate_pi_nilakantha.last_reported_second = current_seconds
                
                error = abs(pi - true_pi)
                
                print(f"Time: {current_seconds} seconds")
                print(f"Iteration {iterations:,}")
                print(f"Current π approximation: {pi}")
                print(f"Error: {error:.15f}")
                print(f"Iterations per second: {iterations/elapsed:.2f}")
                print("-" * 50)
    
    elapsed_time = time.time() - start_time
    return pi, iterations, elapsed_time

def main():
    print("\n" + "="*50)
    print("Pi Calculator - System Information")
    print("="*50)
    
    # Display system information
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")
    
    # Set runtime to 3 minutes (180 seconds) by default
    runtime_seconds = 180
    if len(sys.argv) > 1:
        try:
            runtime_seconds = int(sys.argv[1])
        except ValueError:
            print(f"Invalid runtime value. Using default: {runtime_seconds} seconds")
    
    print("\n" + "="*50)
    print(f"Starting Pi calculation for {runtime_seconds} seconds...")
    print("="*50)
    
    # Record the current time
    start_time = datetime.datetime.now()
    print(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Calculate Pi
    pi_approximation, iterations, elapsed_time = calculate_pi_nilakantha(
        max_runtime_seconds=runtime_seconds
    )
    
    # Display final results
    end_time = datetime.datetime.now()
    print("\n" + "="*50)
    print("Pi Calculation Results")
    print("="*50)
    print(f"Final π approximation: {pi_approximation}")
    print(f"Known value of π:      {math.pi}")
    print(f"Absolute error:        {abs(pi_approximation - math.pi)}")
    print(f"Total iterations:      {iterations:,}")
    print(f"Total runtime:         {elapsed_time:.2f} seconds")
    print(f"Iterations per second: {iterations/elapsed_time:.2f}")
    print(f"End time:              {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)

if __name__ == "__main__":
    main()
