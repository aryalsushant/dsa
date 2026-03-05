import pytest
from conflicts import find_conflicts

def test_main_dataset():
 appointments = [
  {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 10},
  {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 9.5, "end": 10.5},
  {"id": 3, "doctor_id": "D1", "patient_id": "P3", "start": 11, "end": 12},
  {"id": 4, "doctor_id": "D2", "patient_id": "P4", "start": 9, "end": 10},
  {"id": 5, "doctor_id": "D2", "patient_id": "P5", "start": 10, "end": 11},
  {"id": 6, "doctor_id": "D2", "patient_id": "P6", "start": 10.5, "end": 11.5},
  {"id": 7, "doctor_id": "D3", "patient_id": "P7", "start": 8, "end": 9},
  {"id": 8, "doctor_id": "D3", "patient_id": "P8", "start": 9, "end": 10},
 ]
 expected = [(1, 2), (5, 6)]
 assert find_conflicts(appointments) == expected


def test_no_conflicts():
 test_a = [
  {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 10},
  {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 10, "end": 11},
 ]
 expected = []
 assert find_conflicts(test_a) == expected


def test_multiple_conflicts():
 test_b = [
  {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 11},
  {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 10, "end": 12},
  {"id": 3, "doctor_id": "D1", "patient_id": "P3", "start": 10.5, "end": 11.5},
 ]
 expected = [(1, 2), (1, 3), (2, 3)]
 assert find_conflicts(test_b) == expected
