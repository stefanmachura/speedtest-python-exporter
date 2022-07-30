import speedtest

from services import ResultService

servers = []
threads = 1


s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)

results_dict = s.results.dict()

result_dbo = ResultService.create(results_dict)

ResultService.to_file(result_dbo)
