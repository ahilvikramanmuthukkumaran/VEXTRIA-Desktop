from system_info import get_sys_info

def main():
    print("VEXTRIA Desktop is starting ...")
    print("\nSystem Information:")

    info = get_sys_info()

    for key, value in info.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    main()