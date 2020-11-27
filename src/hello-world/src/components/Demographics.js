import React from 'react';

function Demographics(props) {
    return (
        <div className="demographics">
            {/* I believe we're getting rid of
                height, weight and family physician */}
            <p>Name:</p>
            <p>Address:</p>
            <p>DOB:</p>
            <p>Allergies:</p>
            <p>Family History:</p>
            <p>Medical Condition:</p>
            <p>Age:</p>
            <p>Height:</p>
            <p>Weight:</p>
            <p>Medications:</p>
            <p>Family Physician:</p>
        </div>
    );
}

export default Demographics;