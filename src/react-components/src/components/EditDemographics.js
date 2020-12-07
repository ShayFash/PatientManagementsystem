import React, {useState} from 'react';

function EditDemographics(props) {
    const [editName, setEditName] = useState(props.name);
    const [editAddress, setEditAddress] = useState(props.address);
    const [editDOB, setEditDOB] = useState(props.dateOfBirth);
    const [editAllergies, setEditAllergies] = useState(props.allergies);
    const [editCondition, setEditCondition] = useState(props.medicalCondition);
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

    return (
        <form className="demographics"  onSubmit={() => props.setEditing(false)}>
            <button className="navBarButton">Save</button>
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
            <span>Medical Conditions: </span>
            <input value={editCondition} name="medicalConditions" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Age: </span>
            <input value={editAge} name="age" type="text" onChange={handleChange}></input>
            <br/><br/>
            <span>Medications: </span>
            <input value={editMedications} name="medications" type="text" onChange={handleChange}></input>
        </form>
    )
}

export default EditDemographics;