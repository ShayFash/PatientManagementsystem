import React from 'react';
import {Link} from 'react-router-dom';

function ErrorMessage() {
    return (
        <div className="homeContainer">
            <h2>The patient you are looking for is not in the Canadian Health Records Database...</h2>
            <h3>Please try searching again.</h3>
            <Link to="/patientsearch">
                <button className="navBarButton">Search again</button>
            </Link>
        </div>
    )
}

export default ErrorMessage;