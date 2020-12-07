import React from 'react';

function EditDemographics(props) {
    return (
        <div className="demographics">
            <button className="navBarButton" onClick={() => props.setEditing(false)}>Save</button>
            <br/><br/>
            <span>Name: </span>
            <input type="text"></input>
            <br/><br/>
            <span>Address: </span>
            <input type="text"></input>
            <br/><br/>
            <span>DOB: </span>
            <input type="text"></input>
            <br/><br/>
            <span>Medical Conditions: </span>
            <input type="text"></input>
            <br/><br/>
            <span>Age: </span>
            <input type="text"></input>
            <br/><br/>
            <span>Medications: </span>
            <input type="text"></input>
        </div>
    )
}

export default EditDemographics;