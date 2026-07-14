from fastapi import FastAPI

app = FastAPI()

customer_profile = {
    101:{"name":"Raghav", "risk":"low","score":0.12},
    102:{"name":"Rajesh", "risk":"medium","score":0.15},
    103:{"name":"Rajesh", "risk":"high","score":0.18},
    104:{"name":"Rajesh", "risk":"low","score":0.12},
    105:{"name":"Rajesh", "risk":"medium","score":0.15},
    106:{"name":"Rajesh", "risk":"high","score":0.18},
    107:{"name":"Rajesh", "risk":"low","score":0.12},
    108:{"name":"Rajesh", "risk":"medium","score":0.15},
    109:{"name":"Rajesh", "risk":"high","score":0.18},
    110:{"name":"Rajesh", "risk":"low","score":0.12},
}

@app.get("/customer/{customer_id}")

def get_customer_profile(customer_id:int):
    return{
        "customer_id":customer_id
    }
