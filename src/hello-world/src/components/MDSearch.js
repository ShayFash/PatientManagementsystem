import React, {useState} from 'react';

function MDSearch(props) {
    const [specialtySelected, setSpecialtySelected] = useState(false);

    return <SpecialtyList />
}

function SpecialtyList(props) {
    return (
        <ul className="homeContainer" style={{padding:"100px"}}>
            <div>
                
            </div>
        </ul>
    )
}

export default MDSearch;