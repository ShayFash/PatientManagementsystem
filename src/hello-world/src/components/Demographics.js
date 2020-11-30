import React from 'react';

function Demographics(props) {
    return (
        <div className="demographics">
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
    );
}

export default Demographics;