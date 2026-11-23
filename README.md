This is a new project " ClinicFlow "
It is upgraded version of my previous Chatbot creating from scratch: managing patients, readings and appointments.

python 3.12, pytest.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m clinicflow.main
PYTHONPATH=src pytest -v
```




- v0.0: project setup, smoke test
