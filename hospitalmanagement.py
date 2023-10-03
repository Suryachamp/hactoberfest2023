class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")
        print()

class Doctor:
    def __init__(self, doctor_id, name, specialization, contact):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact = contact

    def display_info(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Contact: {self.contact}")
        print()

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def display_info(self):
        print("Appointment Details:")
        print("Patient Information:")
        self.patient.display_info()
        print("Doctor Information:")
        self.doctor.display_info()
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print()

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to the hospital.")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor '{doctor.name}' added to the hospital.")

    def schedule_appointment(self, patient_id, doctor_id, date, time):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)

        if patient and doctor:
            appointment = Appointment(patient, doctor, date, time)
            self.appointments.append(appointment)
            print("Appointment scheduled successfully.")
        else:
            print("Patient or doctor not found. Please check the IDs.")

    def display_appointments(self):
        print("Scheduled Appointments:")
        for appointment in self.appointments:
            appointment.display_info()

def main():
    hospital = Hospital()

    # Adding patients
    patient1 = Patient(1, "John Doe", 30, "Male", "123-456-7890")
    patient2 = Patient(2, "Jane Doe", 25, "Female", "987-654-3210")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Adding doctors
    doctor1 = Doctor(101, "Dr. Smith", "Cardiologist", "555-1234")
    doctor2 = Doctor(102, "Dr. Johnson", "Orthopedic Surgeon", "555-5678")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    # Scheduling appointments
    hospital.schedule_appointment(1, 101, "2023-01-15", "10:00 AM")
    hospital.schedule_appointment(2, 102, "2023-01-20", "02:30 PM")

    # Displaying scheduled appointments
    hospital.display_appointments()

if __name__ == "__main__":
    main()
