import re
import sys

from collections import Counter

class LogsInfo:
    
    def analize_logs(self, path_file: str) -> dict:
        with open(path_file, "r") as file:
            total_lines = 0
            list_userids = []
            set_userids = set()
            response_times = []

            for line in file:
                total_lines += 1
                pattern = r"(user_\d{3}).*?(\d+)ms"
                match = re.search(pattern, line)

                if match:
                    userid = match.group(1)
                    list_userids.append(userid)
                    set_userids.add(userid)


                    time_str = match.group(2)
                    response_times.append(int(time_str))
            
            try:
                average_response_times = sum(response_times) / len(response_times)
            except ZeroDivisionError:
                average_response_times = 0

        return {
            "total_lines": total_lines,
            "average_response_times": f"{average_response_times:.0f}",
            "users": set_userids,
            "most_active_user": Counter(list_userids).most_common(1)
        }
    
if len(sys.argv) < 2:
    print("Use: python3 analyzer.py <path_to_file>")
    sys.exit(1)

test = LogsInfo()
path_file = sys.argv[1]
result = test.analize_logs(path_file)
print(f"Total de linhas lidas: {result["total_lines"]}")
print(f"Tempo médio de resposta: {result["average_response_times"]}ms")
print(f"Todos os usuários capturados: {result["users"]}")
print(f"O Usuário com mais ocorrencias ({result["most_active_user"][0][1]}): {result["most_active_user"][0][0]}")