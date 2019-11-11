import React, { useState, useEffect } from 'react'
import Arrivals from './Arrivals'

const LiveArrivals = ({ match }) => {
    const [arrivalsArray, setArrivalsArray] = useState()
    useEffect(() => {
        if (match.params.smscode) {
            fetch(`http://localhost:8080/api/live-arrivals/${match.params.smscode}`)
                .then(response => {
                    if (!response.ok) {
                        throw Error(response.statusText)
                    }
                    return response
                })
                .then(response => response.json())
                .then(json => setArrivalsArray(json))
                .catch(error => console.log(error))
        }
        if (match.params.naptanid) {
            fetch(`http://localhost:8080/api/live-arrivals/naptan/${match.params.naptanid}`)
                .then(response => {
                    if (!response.ok) {
                        throw Error(response.statusText)
                    }
                    return response
                })
                .then(response => response.json())
                .then(json => setArrivalsArray(json))
                .catch(error => console.log(error))
        }
    }, [match.params.smscode, match.params.naptanid])
    return (
        <div>
            {arrivalsArray ? arrivalsArray.map((arrivals, index) => {
                return <Arrivals key={index} arrivals={arrivals} />
            }) : null}
        </div>
    )
}

export default LiveArrivals
