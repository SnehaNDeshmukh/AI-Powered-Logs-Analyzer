import argparse
import time
from analyzer import LogAnalyzer
from colorama import Fore, Style, init

init(autoreset=True)


def loading_animation():
    """
    Small startup loading effect for professional terminal feel.
    """
    steps = [
        ("[+] Initializing Cyber Threat Detection Engine...", Fore.CYAN),
        ("[+] Loading Machine Learning Model...", Fore.YELLOW),
        ("[+] Loading Log Classification Modules...", Fore.GREEN),
        ("[+] Preparing Report Generation System...", Fore.MAGENTA),
        ("[+] Security Analysis Environment Ready!", Fore.LIGHTGREEN_EX),
    ]

    for step, color in steps:
        print(f"{color}{Style.BRIGHT}{step}{Style.RESET_ALL}")
        time.sleep(0.4)


def banner():
    """
    Premium colorful banner for AI Powered Logs Analyzer
    """
    cyan = Fore.CYAN
    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    magenta = Fore.MAGENTA
    blue = Fore.BLUE
    white = Fore.WHITE
    bright = Style.BRIGHT
    reset = Style.RESET_ALL

    print(f"""{bright}{cyan}
╔════════════════════════════════════════════════════════════════════════════════════════════════════
║                                                                                                       
║   {red} █████╗ ██╗    {yellow}██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ███████╗██████╗    {cyan}    
║   {red}██╔══██╗██║    {yellow}██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔════╝██╔══██╗   {cyan}    
║   {red}███████║██║    {yellow}██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝█████╗  ██║  ██║   {cyan}    
║   {red}██╔══██║██║    {yellow}██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██╔══╝  ██║  ██║   {cyan}    
║   {red}██║  ██║██║    {yellow}██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║███████╗██████╔╝   {cyan}    
║   {red}╚═╝  ╚═╝╚═╝    {yellow}╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝    {cyan} 
║                                                                                                    
║                    {magenta}██╗      ██████╗  ██████╗ ███████╗                              {cyan} 
║                    {magenta}██║     ██╔═══██╗██╔════╝ ██╔════╝                              {cyan} 
║                    {magenta}██║     ██║   ██║██║  ███╗███████╗                              {cyan} 
║                    {magenta}██║     ██║   ██║██║   ██║╚════██║                              {cyan} 
║                    {magenta}███████╗╚██████╔╝╚██████╔╝███████║                              {cyan} 
║                    {magenta}╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝                              {cyan} 
║                                                                                                    
╠════════════════════════════════════════════════════════════════════════════════════════════════════
║  {green}PROJECT TITLE : {white}AI Powered Logs Analyzer                                      {cyan}
║  {green}SUBTITLE      : {white}Intelligent Cybersecurity Log Analysis System                 {cyan}
║  {green}PLATFORM      : {white}Kali Linux Terminal + Python + Machine Learning               {cyan}
║  {green}DEVELOPER     : {blue}Sneha Deshmukh                                                 {cyan}
║  {green}VERSION       : {white}v1.0 Premium Final Year Edition                               {cyan}
║  {green}MODE          : {white}Threat Detection | Log Classification | Report Generation     {cyan}
╚════════════════════════════════════════════════════════════════════════════════════════════════════
{reset}""")


def print_recommendations(recommendations):
    """
    Print recommendations in a styled way.
    """
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════╗")
    print(f"║                    SECURITY RECOMMENDATIONS                 ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

    for rec in recommendations:
        print(f"{Fore.CYAN}  ➜ {Fore.WHITE}{rec}")


def print_footer():
    """
    Professional footer after analysis completes.
    """
    print(f"\n{Fore.GREEN}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════╗")
    print(f"║              ANALYSIS COMPLETED SUCCESSFULLY                ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")


def main():
    parser = argparse.ArgumentParser(
        description="AI Powered Logs Analyzer - Intelligent Cybersecurity Log Analysis System"
    )
    parser.add_argument("logfile", help="Path to the log file to analyze")
    parser.add_argument("--threshold", type=int, default=3, help="Brute force threshold (default: 3)")
    args = parser.parse_args()

    banner()
    loading_animation()

    try:
        analyzer = LogAnalyzer()

        print(f"\n{Fore.LIGHTBLUE_EX}{Style.BRIGHT}[+] Starting analysis on: {args.logfile}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}[+] Brute-force threshold set to: {args.threshold}{Style.RESET_ALL}")

        summary, results, recommendations = analyzer.analyze_logs(
            args.logfile,
            brute_force_threshold=args.threshold
        )

        analyzer.print_results(summary, results)
        analyzer.save_reports(summary, results, recommendations)

        print_recommendations(recommendations)
        print_footer()

    except FileNotFoundError as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}[ERROR] File not found: {e}{Style.RESET_ALL}")

    except ValueError as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}[ERROR] Invalid input: {e}{Style.RESET_ALL}")

    except Exception as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}[ERROR] Unexpected issue: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
