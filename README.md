# 🚦 Uptime Monitor Kubernetes Stack

A simple, automated uptime monitoring solution built with Flask and deployed via Kubernetes and Docker.  
Easily deploy, monitor, and check the health of your endpoints with streamlined shell scripts and Minikube.

---

---

## 🚀 Features

- 🔁 Periodically checks websites for availability (up/down)
- 📶 Displays HTTP response codes and response times
- 📊 Clean HTML dashboard using Flask templating
- ⚙️ Shell scripts for automation (deploy, monitor)
- 📦 Dockerized application
- ☸️ Kubernetes deployment using Minikube (local cluster)

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally using Minikube and Docker:

---

## ☸️ Kubernetes & Docker Setup

1.  **Install Prerequisites:**
    Before you begin, ensure you have the following installed:
    * **Python 3.13.1**
    * **Docker**
    * **Minikube**
    * **kubectl**
    * **Git**
  

2. **Clone the repository:**
    ```
    git clone https://github.com/MiqdadProjects/uptime-monitor.git

    cd uptime-monitor
    ```

3. **Start Minikube:**
    ```
    minikube start
    ```


4.  **Build and Deploy the Application:**
    Navigate to the project root and execute the deployment script. This script handles everything from Docker image creation to Kubernetes manifest application.
    ```bash
    chmod +x scripts/*.sh # Grant execute permissions to scripts
    
    ./scripts/deploy.sh
    ```
    This script will:
    * Build the Docker image directly within Minikube’s Docker daemon.
    * Apply the necessary Kubernetes manifests (Deployment and Service).
    * Expose the Flask application service via Minikube.

      
       

5. **Access the application:**  
   The script will display a URL (e.g., `http://192.168.49.2:30007`)
   
   Open this URL in your browser to access the Flask uptime monitor.

   
   

6. **Monitor uptime with the monitoring script:**
    ```
    ./scripts/monitor.sh
    ```
    This will run the Python monitoring script and log results to `db.json`.
   

7. **Stopping Minikube:**
    ```
    minikube stop
    ```

---

## 🛠 Local Development (Optional)

### Backend (Flask)

1. **Set up a Python virtual environment:**
    ```
    python3 -m venv venv

    source venv/bin/activate  # On Windows: venv\Scripts\activate

    ```

2. **Install dependencies:**
    ```
    pip install -r backend/requirements.txt
    ```

3. **Run the Flask app locally:**
    ```
    cd backend
    python app.py
    ```
    The API will be available at [http://localhost:5000](http://localhost:5000).

---

## 📝 Monitoring Script

The monitoring script (`monitor.py`) checks the status of configured endpoints and writes results to `db.json`.

To run it manually:

 ```
./scripts/monitor.sh

 ```


You can schedule this script to run at intervals using a cron job or Windows Task Scheduler.

---

## 💡 Tips

- Ensure you run `deploy.sh` from the project root or use the provided script path.  
- If you modify the backend code, re-run `./scripts/deploy.sh` to rebuild the Docker image and update the deployment.  
- All deployment and monitoring logic is automated for ease of use.  
- For custom endpoints, edit the monitoring script as needed.  

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

**Happy monitoring! 🚦**

