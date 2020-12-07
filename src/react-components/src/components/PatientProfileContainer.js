import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import NavBar from './NavBar';
import Demographics from './Demographics';
import EditDemographics from './EditDemographics';
import ErrorMessage from './ErrorMessageContainer';

function PatientProfileContainer(props) {
    // patient state variables
    // editable
    const [name, setName] = useState("");
    const [address, setAddress] = useState("");
    const [dateOfBirth, setDateOfBirth] = useState("");
    const [allergies, setAllergies] = useState("");
    const [medicalCondition, setMedicalCondition] = useState("");
    const [age, setAge] = useState("");
    const [medications, setMedications] = useState("");
    const [familyHistory, setFamilyHistory] = useState("");
    // non-editable
    const [federalHealthID, setFederalHealthID] = useState("");
    const [genderID, setGenderID] = useState("");
    const [patientID, setPatientID] = useState("");
    const [provinceID, setProvinceID] = useState("");
    const [temp, setTemp] = useState("");

    // react functionality variables
    const [editing, setEditing] = useState(false);
    const [fetchError, setFetchError] = useState(false);

    let {num} = useParams();

    // called as a componentDidUpdate substitute but only when num changes
    // called as a componentDidUnmount, reverts fetchError back to false
    useEffect(() => {
        console.log("Fetched");
        fetch(`http://localhost:5000/get/patient/${num}`)
        .then(response => response.json())
        .then(data => {
            setName(data.name);
            setAddress(data.address);
            setDateOfBirth(data.dateOfBirth);
            setAllergies(data.allergies);
            setMedicalCondition(data.medicalConditions);
            setAge(data.age);
            setMedications(data.medications);
            setFamilyHistory(data.familyHistory);
            setFederalHealthID(data.federalHealthID);
            setGenderID(data.genderID);
            setPatientID(data.patientID);
            setProvinceID(data.provinceID);
            setTemp(data.temp);
        }, () => {
            setFetchError(true);
        })
        return () => {
            setFetchError(false);
        }
    }, [num]);

    return (
        <div>    
            {fetchError ? 
                <ErrorMessage /> :
                <div className="patientProfileContainer">
                    {editing ? 
                    <EditDemographics name={name} address={address}
                            dateOfBirth={dateOfBirth}
                            allergies={allergies} medicalCondition = {medicalCondition}
                            age={age} medications={medications} familyHistory={familyHistory}
                            setEditing={setEditing}
                            federalHealthID={federalHealthID}
                            genderID={genderID}
                            patientID={patientID}
                            provinceID={provinceID}
                            temp={temp}
                            /> :
                    <Demographics name={name} address={address}
                            dateOfBirth={dateOfBirth}
                            allergies={allergies} medicalCondition = {medicalCondition}
                            age={age} medications={medications} familyHistory={familyHistory}
                            setEditing={setEditing}/>
                    }
                    <NavBar />
                </div>
            }
        </div>
    );
}

export default PatientProfileContainer;