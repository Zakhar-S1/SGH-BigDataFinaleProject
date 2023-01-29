Description:
1. I created an application with streaming data processing. It analyzes a dataset from Kaggle (link: https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers). 
2. I used Docker, Kafka, PostgreSQL, Spark, Python. It filters the data, and then the result is exported to an Excel spreadsheet, where you can further build graphs. 
3. In Kafka, I load data unloaded from dataset for temporary storage, that is, Kafka is used as a data bus. 
4. In the database I already store all the data after stream processing and filtering. 

Instructions:
1. Install docker and docker compose on the host machine
2. Run: make build (make command from Makefile) == docker-compose build
3. Run: make up (make command from Makefile) == docker-compose up
    + To put down the containers: make down (make command from Makefile) == docker-compose down
4. Running in three different terminals:
    + docker run -it zahar_project_producer sh
    + docker run -it zahar_project_spark_streaming sh
    + docker run -it zahar_project_analytics sh
5. In addition, you must create: network project_global_network , so the containers can see each other
6. Add our 3 containers to the docker network, for this purpose do:
    1. Prescribe: docker ps, to find all of our ids of the containers we have previously lifted
    2. Run them through with a command: docker network connect project_global_network def48f545dff
        + You can check it with a command: docker network inspect project_global_network
7. Check in containers for ip to postgress in the container: spark_streaming и analytics (ip you can look through the same Network Inspector)    
    + Also check the IP address of the master container spark в spark_streaming
8. Running the command in the container: producer python3 ./main.py --file_path /producer/CreditCardCustomers.csv --topic_name data --file_format csv --type_of_producer kafka
    + Check the data in kafka ui по адрессу http://localhost:8080/ui/clusters/local/topics
9. Run the command in the container spark python3 ./streaming.py, filter data
    + Check the data in PostgreSQL
10. Run in a container: analytics python3 ./main.py  and check that the container contains files with statistics
11. Get the files on the host machine with the command: docker cp sharp_torvalds(container name):/analytics/income_category_info.xlsx .
    + You can see the name of the files in analytics/queries/queries.py
