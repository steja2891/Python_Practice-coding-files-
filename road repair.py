crew_id_count = int(input().strip())

crew_id = []

for _ in range(crew_id_count):
    crew_id_item = int(input().strip())
    crew_id.append(crew_id_item)

job_id_count = int(input().strip())

job_id = []

for _ in range(job_id_count):
    job_id_item = int(input().strip())
    job_id.append(job_id_item)
crew_id.sort()
a =[]
for i in crew_id:
    b = []
    for j in job_id:
            b.append(j-i)
    a.append(abs(min(b)))
    job_id.remove(min(b)+i)
print(sum(a))