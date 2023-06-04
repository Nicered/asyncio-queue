import asyncio
import uuid
import time



class Hub:
    # 크롤러 클래스와 래핑 클래스의 비동기적 태스크를 관리하는 클래스
    def __init__(self):                
        self.queue = asyncio.Queue()    
        self.is_finished = False         
        
    
    async def publisher(self,data_list):
        # function for put tasks
        for data in data_list:
            print("Put data in Queue:{}".format(data))
            # implement slow work
            await asyncio.sleep(2)
            await self.queue.put(post)            
            print(self.queue)
            if post == post_list[-1]:
                self.is_finshed = True
                
    async def subscriber(self):        
        while True:
            if self.is_finished and self.queue.empty():
                # it is condition for stopped loop
                break
            print("subscriber is running")                        
            try:
                data = await self.queue.get()
                print("subscriber data:{}".format(data))
                self.queue.task_done()
            except asyncio.QueueEmpty:
                print("Queue is empty")   
                
    async def start(self):
       # start two task async
        post_data = init_data()
        tasks = [self.publisher(post_data),self.subscriber()]
        await asyncio.gather(*tasks)
    
def init_data():
   # Generate test data
    data_list = [uuid.uuid4() for i in range(100)]
    return data_list   
       
    
    
if __name__ == "__main__":
    cls = Hub()    
    asyncio.run(cls.start())
