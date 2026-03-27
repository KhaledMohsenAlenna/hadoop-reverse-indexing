# The Digital Librarian: Distributed Reverse Indexing
**Team Members:**
- Khaled Mohsen Abdellatif (ID: 202201198)
- Omar El-Desouky (ID: 202202155)

## Files Included
- `mapper.py`: Tokenizes text, removes punctuation and stop-words.
- `combiner.py`: Performs local aggregation to optimize network shuffle.
- `reducer.py`: Aggregates final word counts and formats the reverse index.
- `stopwords.txt`: List of words to filter out.

## Execution Instructions
To execute this job on a Hadoop cluster, run the following Hadoop Streaming command:

```bash
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
  -files mapper.py,combiner.py,reducer.py,stopwords.txt \
  -mapper "python3 mapper.py" \
  -combiner "python3 combiner.py" \
  -reducer "python3 reducer.py" \
  -input /user/student/library \
  -output /user/student/output_cluster
