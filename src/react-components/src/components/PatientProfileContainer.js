import React, {useState, useEffect} from 'react';
import NavBar from './NavBar';
import Demographics from './Demographics';

function PatientProfileContainer() {
    const [name, setName] = useState("");
    const [address, setAddress] = useState("");
    const [dateOfBirth, setDateOfBirth] = useState("");
    const [allergies, setAllergies] = useState("");
    const [medicalCondition, setMedicalCondition] = useState("");
    const [age, setAge] = useState("");
    const [medications, setMedications] = useState("");

    useEffect(() => {
        fetch("http://127.0.0.1:5000/get/patient/0")
        .then(response => response.json())
        .then(data => {
            setName(data.name);
            setAddress(data.address);
            setDateOfBirth(data.dateOfBirth);
            setAllergies(data.allergies);
            setMedicalCondition(data.medicalCondition);
            setAge(data.age);
            setMedications(data.medications)
        }, error => console.log("Error"))
    }, []);
    return (
        <div className="patientProfileContainer">
            <Demographics name={name} address={address}
                          dateOfBirth={dateOfBirth}
                          allergies={allergies} medicalCondition = {medicalCondition}
                          age={age} medications={medications}/>
            <NavBar />
        </div>
    );
}

export default PatientProfileContainer;