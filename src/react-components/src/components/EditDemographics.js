import React, {useState} from 'react';

function EditDemographics(props) {
    // patient state variables
    const [editName, setEditName] = useState(props.name);
    const [editAddress, setEditAddress] = useState(props.address);
    const [editDOB, setEditDOB] = useState(props.dateOfBirth);
    const [editAllergies, setEditAllergies] = useState(props.allergies);
    const [editCondition, setEditCondition] = useState(props.medicalCondition);
    const [editFamilyHistory, setEditFamilyHistory] = useState(props.familyHistory)

    // react functionality state variables
    const [editAge, setEditAge] = useState(props.age);
    const [editMedications, setEditMedications] = useState(props.medications);

    function handleChange(event) {
        const {value} = event.target;
        switch(event.target.name) {
            case "name":
                setEditName(value);
                break;
            case "address":
                setEditAddress(value);
                break;
            case "dateOfBirth":
                setEditDOB(value);
                break;
            case "allergies":
                setEditAllergies(value);
                break;
            case "familyHistory":
                setEditFamilyHistory(value);
                break;
            case "medicalConditions":
                setEditCondition(value);
                break;
            case "age":
                setEditAge(value);
                break;
            case "medications":
                setEditMedications(value);
                break;
            default:
                console.log("Somthing went wrong");
                break;
        }
    }

    const handleSubmit = async (event) => {
        const data = {
            federalHealthID: props.federalHealthID,
            provinceID: props.provinceID,
            name: editName,
            genderID: props.genderID,
            dateOfBirth: editDOB,
            age: editAge,
            temp: props.temp,
            address: editAddress,
            familyHistory: editFamilyHistory,
            medicalConditions: editCondition,
        }
        
        await fetch("http://localhost:5000/post/create_patient", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(() => { 
            props.setEditing(false);
            window.location.reload();
        })
        .catch(error => {
            console.error("Error: ", error)
        })
    }

    return (
        <div className="demographics">
            <button className="navBarButton" onClick={handleSubmit}>Save</button>
            <br/><br/>
            <span>Name: </span>
            <input value={editName} name="name" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Address: </span>
            <input value={editAddress} name="address" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>DOB: </span>
            <input value={editDOB} name="dateOfBirth" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Allergies: </span>
            <input value={editAllergies} name="allergies" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Family History: </span>
            <input value={editFamilyHistory} name="familyHistory" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Medical Conditions: </span>
            <input value={editCondition} name="medicalConditions" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Age: </span>
            <input value={editAge} name="age" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Medications: </span>
            <input value={editMedications} name="medications" type="text" onChange={handleChange}></input>
        </div>
    )
}

export default EditDemographics;