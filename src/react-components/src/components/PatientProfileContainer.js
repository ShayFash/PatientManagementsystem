import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import NavBar from './NavBar';
import Demographics from './Demographics';
import ErrorMessage from './ErrorMessageContainer';

function PatientProfileContainer() {
    const [name, setName] = useState("");
    const [address, setAddress] = useState("");
    const [dateOfBirth, setDateOfBirth] = useState("");
    const [allergies, setAllergies] = useState("");
    const [medicalCondition, setMedicalCondition] = useState("");
    const [age, setAge] = useState("");
    const [medications, setMedications] = useState("");
    const [fetchError, setFetchError] = useState(false);

    let {num} = useParams();

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/get/patient/${num}`)
        .then(response => response.json())
        .then(data => {
            setName(data.name);
            setAddress(data.address);
            setDateOfBirth(data.dateOfBirth);
            setAllergies(data.allergies);
            setMedicalCondition(data.medicalCondition);
            setAge(data.age);
            setMedications(data.medications);
        }, () => {
            setFetchError(true);
        })
    }, [num]);
    return (
        <div>    
            {fetchError ? 
                <ErrorMessage /> :
                <div className="homeContainer">
                    <Demographics name={name} address={address}
                            dateOfBirth={dateOfBirth}
                            allergies={allergies} medicalCondition = {medicalCondition}
                            age={age} medications={medications}/>
                    <NavBar />
                </div>
            }
        </div>
    );
}

export default PatientProfileContainer;