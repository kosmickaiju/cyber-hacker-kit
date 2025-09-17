import argparse
import sys
import time
from datetime import datetime

def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    Purple Team Toolkit                       ║
    ║                                                              ║
    ║  Comprehensive Cybersecurity Training and Assessment Tools   ║
    ║                                                              ║
    ║  🛡️  Cyber Hygiene: Personal security assessment              ║
    ║  🎯 Ethical Hacker: Advanced penetration testing tools        ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def run_hygiene_toolkit():
    """Run the Cyber Hygiene toolkit with improved interface"""
    from scanners import password_checker, hygiene_port_scan
    import hygiene_summary
    
    print("\n Cyber Hygiene Toolkit")
    print("=" * 50)
    
    tools = {
        '1': {
            'name': 'Password Checker',
            'description': 'Check if your password has been compromised in data breaches',
            'function': password_checker.password_check
        },
        '2': {
            'name': 'Port Scanner',
            'description': 'Scan your system for open ports',
            'function': hygiene_port_scan.run_scan
        },
        '3': {
            'name': 'Complete Hygiene Summary',
            'description': 'Run both tools and get personalized recommendations',
            'function': hygiene_summary.run_summary
        }
    }
    
    while True:
        print("\nAvailable tools:")
        for key, tool in tools.items():
            print(f"  {key}. {tool['name']} - {tool['description']}")
        print("  0. Return to main menu")
        
        choice = input("\nSelect a tool (1-3) or 0 to exit: ").strip()
        
        if choice == '0':
            break
        elif choice in tools:
            tool = tools[choice]
            print(f"\n🔄 Loading {tool['name']}...")
            print("-" * 40)
            time.sleep(1)
            
            try:
                tool['function']()
            except KeyboardInterrupt:
                print("\n⚠️  Tool interrupted by user")
            except Exception as e:
                print(f"❌ Error running {tool['name']}: {e}")
            
            input("\nPress Enter to continue...")
        else:
            print("❌ Invalid choice. Please try again.")

def run_hacker_toolkit():
    """Run the Ethical Hacker toolkit with improved interface"""
    try:
        from scanners import (network_scan, hacker_port_scan, packet_sniffer, 
                            vuln_scanner, password_cracker, hash_cracker)
    except ImportError as e:
        print(f"❌ Error importing hacker tools: {e}")
        print("Some tools may require additional dependencies.")
        return
    
    print("\n🎯 Ethical Hacker Training Toolkit")
    print("=" * 50)
    print("⚠️  WARNING: These tools are for educational and authorized testing only!")
    print("   Only use on systems you own or have explicit permission to test.")
    
    tools = {
        '1': {
            'name': 'Network Scanner',
            'description': 'Discover devices on a network range',
            'function': lambda: network_scan.run(input("Enter network range (e.g., 192.168.1.0/24): "))
        },
        '2': {
            'name': 'Port Scanner',
            'description': 'Scan a target for open ports',
            'function': lambda: hacker_port_scan.run(input("Enter target IP: "))
        },
        '3': {
            'name': 'Packet Sniffer',
            'description': 'Capture and analyze network packets',
            'function': packet_sniffer.run
        },
        '4': {
            'name': 'Vulnerability Scanner',
            'description': 'Scan for common vulnerabilities',
            'function': lambda: vuln_scanner.run(input("Enter target IP: "))
        },
        '5': {
            'name': 'Password Cracker',
            'description': 'SSH brute force testing (educational)',
            'function': run_password_cracker
        },
        '6': {
            'name': 'Hash Cracker',
            'description': 'Crack password hashes using wordlists',
            'function': run_hash_cracker
        }
    }
    
    while True:
        print("\nAvailable tools:")
        for key, tool in tools.items():
            print(f"  {key}. {tool['name']} - {tool['description']}")
        print("  0. Return to main menu")
        
        choice = input("\nSelect a tool (1-6) or 0 to exit: ").strip()
        
        if choice == '0':
            break
        elif choice in tools:
            tool = tools[choice]
            
            # Ethical use confirmation
            confirm = input(f"\n⚠️  Are you authorized to use {tool['name']} on the target? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Operation cancelled. Only use tools on authorized targets.")
                continue
            
            print(f"\n🔄 Loading {tool['name']}...")
            print("-" * 40)
            time.sleep(1)
            
            try:
                result = tool['function']()
                if result and isinstance(result, str):
                    print(result)
            except KeyboardInterrupt:
                print("\n⚠️  Tool interrupted by user")
            except Exception as e:
                print(f"❌ Error running {tool['name']}: {e}")
            
            input("\nPress Enter to continue...")
        else:
            print("❌ Invalid choice. Please try again.")

def run_password_cracker():
    """Wrapper for password cracker with safety warnings"""
    print("⚠️  SSH Password Cracker - Educational Use Only!")
    print("This tool demonstrates brute force attacks for learning purposes.")
    print("NEVER use this on systems you don't own or lack permission to test.")
    
    confirm = input("\nDo you understand and agree to ethical use? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Operation cancelled.")
        return
    
    hostname = input("Enter target hostname/IP: ")
    username = input("Enter username to test: ")
    
    print(f"\nStarting educational brute force demonstration against {hostname}")
    print("This would typically test weak passwords like: admin, password, 123456, etc.")
    print("In a real scenario, this could take hours or days with larger wordlists.")
    
    # Simulate the process without actual execution
    test_passwords = ["admin", "password", "123456", "letmein", "guest"]
    for i, pwd in enumerate(test_passwords):
        time.sleep(0.5)
        print(f"Testing password {i+1}/5: {pwd} - Failed")
    
    print("\nDemo completed. No passwords were actually tested.")
    print("Remember: Use strong, unique passwords and enable 2FA!")

def run_hash_cracker():
    """Wrapper for hash cracker with educational content"""
    print("🔐 Hash Cracker - Educational Tool")
    print("This demonstrates how weak passwords can be cracked from hash values.")
    
    hash_type = input("Hash type (md5/sha1/sha256): ").lower()
    if hash_type not in ['md5', 'sha1', 'sha256']:
        print("Unsupported hash type for this demo.")
        return
    
    target_hash = input("Enter hash to crack: ").strip()
    
    print(f"\nThis would attempt to crack the {hash_type.upper()} hash using:")
    print("• Dictionary attacks with common passwords")
    print("• Wordlist-based attacks")
    print("• Rainbow table lookups")
    
    print("\nDemo mode - no actual cracking performed.")
    print("Real hash cracking requires:")
    print("• Large wordlists (rockyou.txt, etc.)")
    print("• Powerful hardware (GPUs)")
    print("• Significant time investment")
    print("\n💡 Defense: Use long, complex passwords with salting!")

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description='Purple Team Toolkit - Cybersecurity Training and Assessment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --gui              Launch graphical interface
  python main.py --hygiene          Run cyber hygiene tools
  python main.py --hacker           Run ethical hacker tools
  python main.py --version          Show version information
        """
    )
    
    parser.add_argument('--hygiene', action='store_true',
                       help='Run Cyber Hygiene toolkit (password checker, port scanner)')
    parser.add_argument('--hacker', action='store_true',
                       help='Run Ethical Hacker toolkit (advanced penetration testing tools)')
    parser.add_argument('--gui', action='store_true',
                       help='Launch graphical user interface')
    parser.add_argument('--version', action='version', version='Purple Team Toolkit v2.0')
    
    args = parser.parse_args()
    
    # If no arguments provided, show interactive menu
    if not any(vars(args).values()):
        print_banner()
        
        while True:
            print(f"\n📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("\nMain Menu:")
            print("  1. Launch GUI Interface")
            print("  2. Cyber Hygiene Toolkit")
            print("  3. Ethical Hacker Toolkit") 
            print("  4. Show Help")
            print("  0. Exit")
            
            choice = input("\nSelect an option (0-4): ").strip()
            
            if choice == '0':
                print("\n👋 Thank you for using Purple Team Toolkit!")
                sys.exit(0)
            elif choice == '1':
                print("\n🖥️  Launching GUI...")
                try:
                    from gui import PurpleTeamGUI
                    app = PurpleTeamGUI()
                    app.run()
                except ImportError:
                    print("❌ GUI not available. Please check gui.py exists.")
                except Exception as e:
                    print(f"❌ Error launching GUI: {e}")
            elif choice == '2':
                run_hygiene_toolkit()
            elif choice == '3':
                run_hacker_toolkit()
            elif choice == '4':
                parser.print_help()
            else:
                print("❌ Invalid choice. Please try again.")
    
    else:
        # Handle command line arguments
        if args.gui:
            print("🖥️  Launching GUI...")
            try:
                from gui import PurpleTeamGUI
                app = PurpleTeamGUI()
                app.run()
            except ImportError:
                print("❌ GUI not available. Please check gui.py exists.")
            except Exception as e:
                print(f"❌ Error launching GUI: {e}")
                
        elif args.hygiene:
            print_banner()
            run_hygiene_toolkit()
            
        elif args.hacker:
            print_banner()
            run_hacker_toolkit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application terminated by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)