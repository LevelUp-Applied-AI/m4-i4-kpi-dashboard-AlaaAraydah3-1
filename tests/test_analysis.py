"""Tests for the KPI dashboard analysis.

Write at least 3 tests:
1. test_extraction_returns_dataframes — extract_data returns a dict of DataFrames
2. test_kpi_computation_returns_expected_keys — compute_kpis returns a dict with your 5 KPI names
3. test_statistical_test_returns_pvalue — run_statistical_tests returns results with p-values
"""
from analysis import connect_db, extract_data, compute_kpis, run_statistical_tests
import pandas as pd

def test_extraction_returns_dataframes():
    engine = connect_db()
    data = extract_data(engine)
    assert isinstance(data, dict)
    for table in ["customers", "products", "orders", "order_items"]:
        assert table in data
        assert isinstance(data[table], pd.DataFrame)

def test_kpi_computation_returns_expected_keys():
    engine = connect_db()
    data = extract_data(engine)
    kpis = compute_kpis(data)
    for key in ["Total Revenue", "Average Order Value", "Customer Retention Rate",
                "Monthly Active Users", "Cohort Revenue Growth", "merged_data"]:
        assert key in kpis

def test_statistical_test_returns_pvalue():
    engine = connect_db()
    data = extract_data(engine)
    kpis = compute_kpis(data)
    stat_results = run_statistical_tests(kpis)
    assert "city_comparison" in stat_results
    p_val = stat_results["city_comparison"].get("p_value")
    assert p_val is not None
    assert 0 <= p_val <= 1