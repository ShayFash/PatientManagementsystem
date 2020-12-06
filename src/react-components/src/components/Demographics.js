import React from 'react';

function Demographics(props) {
    let imageName = require('../img/edit_icon.png');
    return (
        <div className="demographics">
            <div>
                {/* I believe we're getting rid of
                height, weight and family physician */}
                <p>Name: {props.name}</p>
                <p>Address: {props.address}</p>
                <p>DOB: {props.dateOfBirth}</p>
                <p>Allergies: {props.allergies}</p>
                {/* <p>Family History: {props.familyHistory}</p> */}
                <p>Medical Condition: {props.medicalCondition}</p>
                <p>Age: {props.age}</p>
                {/* <p>Height:</p>
                <p>Weight:</p> */}
                <p>Medications: {props.medications}</p>
                {/* <p>Family Physician:</p> */}
            </div>
            <div>
                <img src={imageName.default} alt="require function fails" style={{width: "50px", height: "50px"}}/>
            </div>
        </div>
    );
}

export default Demographics;