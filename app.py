from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class SurveyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    household_size = db.Column(db.Integer, nullable=False)
    house_size = db.Column(db.Integer, nullable=False)
    home_type = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    appliances = db.Column(db.String(200), nullable=True)
    appliance_age = db.Column(db.Integer, nullable=False)
    appliance_usage = db.Column(db.Integer, nullable=False)
    energy_efficiency = db.Column(db.String(3), nullable=False)
    lighting_type = db.Column(db.String(100), nullable=False)
    lighting_usage = db.Column(db.Integer, nullable=False)
    energy_conservation_habits = db.Column(db.String(200), nullable=True)
    peak_usage_awareness = db.Column(db.String(3), nullable=False)
    usage_during_peak_hours = db.Column(db.String(10), nullable=False)
    average_bill = db.Column(db.Integer, nullable=False)
    renewable_energy = db.Column(db.String(3), nullable=False)
    energy_efficiency_interest = db.Column(db.Integer, nullable=False)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    new_data = SurveyData(
        household_size=data['householdSize'],
        house_size=data['houseSize'],
        home_type=data['homeType'],
        location=data['location'],
        appliances=','.join(request.form.getlist('appliances')),
        appliance_age=data['applianceAge'],
        appliance_usage=data['applianceUsage'],
        energy_efficiency=data['energyEfficiency'],
        lighting_type=data['lightingType'],
        lighting_usage=data['lightingUsage'],
        energy_conservation_habits=','.join(request.form.getlist('energyConservationHabits')),
        peak_usage_awareness=data['peakUsageAwareness'],
        usage_during_peak_hours=data['usageDuringPeakHours'],
        average_bill=data['averageBill'],
        renewable_energy=data['renewableEnergy'],
        energy_efficiency_interest=data['energyEfficiencyInterest']
    )
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
