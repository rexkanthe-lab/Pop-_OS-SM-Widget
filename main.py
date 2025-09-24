# Import necessary libraries
import psutil
import GPUtil
import time

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get RAM usage
def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.percent

# Function to get GPU usage
def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    return [{"id": gpu.id, "gpu_load": gpu.load * 100} for gpu in gpus]

# Function to get thermal sensors
def get_temperature():
    temperatures = psutil.sensors_temperatures()
    return {temp: temps for temp, temps in temperatures.items() if temps}

# Main monitoring loop
if __name__ == '__main__':
    while True:
        print(f"CPU Usage: {get_cpu_usage()}%")
        print(f"RAM Usage: {get_ram_usage()}%")
        print(f"GPU Usage: {get_gpu_usage()}")
        print(f"Temperature: {get_temperature()}")
        time.sleep(5)
