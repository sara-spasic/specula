
from sqlalchemy import inspect
from app.api.models import *


def assert_relationship(model, relationship_name, target_model):
    relationships = inspect(model).relationships

    assert relationship_name in relationships

    relationship = relationships[relationship_name]
    assert relationship.mapper.class_ is target_model


def test_ioc_relationships():
    assert_relationship(
        IOC, "source_observations", SourceObservation
    )
    assert_relationship(
        IOC, "risk_assessments", RiskAssessment
    )


def test_source_observation_relationships():
    assert_relationship(
        SourceObservation, "source", Source
    )
    assert_relationship(
        SourceObservation, "ioc", IOC
    )


def test_source_relationships():
    assert_relationship(
        Source, "observations", SourceObservation
    )


def test_risk_assessment_relationships():
    assert_relationship(
        RiskAssessment, "ioc", IOC
    )


def test_file_behaviour_relationships():
    assert_relationship(
        FileBehaviour, "file", File
    )
    assert_relationship(
        FileBehaviour, "mitre_techniques", MITREtechnique
    )
    assert_relationship(
        FileBehaviour, "sigma_analyses", SigmaAnalysis
    )
    assert_relationship(
        FileBehaviour, "signature_matches", SignatureMatch
    )
    assert_relationship(
        FileBehaviour, "process_activities", ProcessActivity
    )
    assert_relationship(
        FileBehaviour, "file_activities", FileActivity
    )
    assert_relationship(
        FileBehaviour, "service_activities", ServiceActivity
    )