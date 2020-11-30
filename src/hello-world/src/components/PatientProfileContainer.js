import React from 'react';
import NavBar from './NavBar';
import Demographics from './Demographics';

function PatientProfileContainer() {
    return (
        <div className="patientProfileContainer">
            <Demographics name="John Doe" address="123 Sesame Street" 
                          dateOfBirth="January 1st 1980"
                          allergies="Peanuts" medicalCondition = "Broken Leg"
                          age={40} medications="Adderall"/>
            <NavBar />
        </div>
    );
}

export default PatientProfileContainer;