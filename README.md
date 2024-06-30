# Event Monitoring and Alerting System

This project implements an event monitoring and alerting system. It simulates the generation of different types of events and monitors them using predefined alert configurations. When a threshold is breached, the system dispatches alerts via different strategies such as console output or email.

## Requirements

- Python 3.10+

## Project Structure

- `alerting_system/`
  - `event.py`: Contains the `Event` class representing an event.
  - `monitoring.py`: Contains the `MonitoringService` class that monitors events and triggers alerts.
  - `dispatcher.py`: Contains classes for dispatching alerts via different strategies.
  - `config.py`: Contains the configuration for alerts.
- `literals/`
  - `counts.py`: Defines constants for the number of different types of events.
  - `enums.py`: Defines enums for alert types, event types, and dispatch types.
  - `messages.py`: Defines messages for logs.
- `constants/`
  - `alert_configs.py`: Contains the alert configurations.
- `main.py`: Main file.
- `output.png`: Sample console screenshot.
- `utils/`
  - `logs_formatter.py`: Contains util functions for console formatting.
## How to Run

1. Clone the repository.
2. Run the `main.py` script.

```bash
python main.py
```

## Main Function

The `main` function simulates the generation of events and processes them using the `MonitoringService`. 

### Explanation

1. **Initialize Monitoring Service:** The `MonitoringService` is initialized with predefined alert configurations.
2. **Generate Events:** Different types of events are generated for different clients:
   - `PAYMENT_EXCEPTION` events for client X.
   - `USERSERVICE_EXCEPTION` events for client X.
   - `LOGIN_FAILURE` events for client Y.
3. **Process Events:** Each event is processed by the `MonitoringService` to check if any alert thresholds are breached.

## Adding New Event Types

To add new event types:
1. Define the event type in `literals/enums.py`.
2. Update the event generation logic in the `main` function.
3. Add corresponding alert configurations in `constants/alert_configs.py`.

## Extending Alert Dispatch Strategies

To add new alert dispatch strategies:
1. Define the new dispatch type in `literals/enums.py`.
2. Implement the dispatch logic in `alerting_system/dispatcher.py`.
3. Update alert configurations to use the new dispatch strategy.

## License

This project is licensed under the MIT License.

---

This README provides an overview of the project, its structure, how to run it, and guidelines for extending the functionality.