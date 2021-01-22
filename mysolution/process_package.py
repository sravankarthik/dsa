class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def Process(self, request):
        while len(self.finish_time)>0 and self.finish_time[0]<=request.arrival_time:
            self.finish_time.pop(0)
        if len(self.finish_time)<self.size:
            if len(self.finish_time)==0:
                self.finish_time.append(request.arrival_time+request.process_time)
                return Response(True, request.arrival_time)
            else:
                if request.arrival_time<self.finish_time[-1]:
                    x = self.finish_time[-1]
                elif request.arrival_time==self.finish_time[-1]:
                    x = 1 + self.finish_time[-1]
                self.finish_time.append(x + request.process_time)
                return Response(True, x)

        else:
            return Response(False, request.arrival_time)





def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses


def PrintResponses(responses):
    for response in responses:
        print(response.start_time if response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)




