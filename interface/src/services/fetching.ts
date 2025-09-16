import HOSPITALS from "@/misc/url";
import hospitalInfoData from "@/types/hospitalInfoData";

interface hospitalInfoProps {
    hospitalInfo: hospitalInfoData[];
    setHospitalInfo: (value: hospitalInfoData[]) => void;
    targetHospital :HOSPITALS;
}

const getHospitalInfo = (props :hospitalInfoProps) => {

    let config :RequestInit = {
        method: "GET",
        mode: "cors"
    }



    let hospitalInfoPromise = fetch("http://127.0.0.1:5001/api/hospital", config).then((hospitalDataRaw :Response) => {
        hospitalDataRaw.json().then((hospitalInfo) => {
            let hosInfo = hospitalInfo as hospitalInfoData[];
            props.setHospitalInfo(hosInfo)

        }) 
    })
}


export default getHospitalInfo;        