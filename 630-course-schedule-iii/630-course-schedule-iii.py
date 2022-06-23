class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        # print(courses)
        heap = []
        timeSofar = 0
        for course in courses:
            if timeSofar + course[0] <= course[1]:
                heappush(heap, -course[0])
                timeSofar += course[0]
            elif heap:
                top = -heappop(heap)
                if top > course[0]:
                    timeSofar -= top
                    heappush(heap, -course[0])
                    timeSofar += course[0]
                else:
                    heappush(heap, -top)
        # print(heap)
        return len(heap)
                
            